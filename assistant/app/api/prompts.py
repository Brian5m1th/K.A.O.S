import uuid
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from loguru import logger

from app.database import get_session
from app.models.prompt import Prompt

router = APIRouter(prefix="/api/prompts", tags=["Prompts"])


class PromptSchema(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    category: str = Field(..., pattern="^(coding|writing|ux|system)$")
    prompt: str = Field(..., min_length=1)
    description: str = Field(..., min_length=1)


class PromptResponse(PromptSchema):
    id: str


INITIAL_PROMPTS = [
    {
        "title": "Code Reviewer Pro",
        "category": "coding",
        "description": "Revisa código procurando por bugs, gargalos de performance e riscos de segurança.",
        "prompt": "Aja como um engenheiro de software sênior. Revise as alterações de código a seguir analisando: complexidade ciclomática, vazamentos de memória e conformidade com clean code.",
    },
    {
        "title": "Technical Spec Writer (SDD)",
        "category": "writing",
        "description": "Estrutura discussões e ideias em documentos formais de SDD (Software Design Document).",
        "prompt": "Escreva um Software Design Document (SDD) estruturado baseado no seguinte backlog de decisões técnicas. Inclua seções de Objetivo, Requisitos Funcionais, Arquitetura Proposta e Plano de Verificação.",
    },
    {
        "title": "Tailwind UI Designer",
        "category": "ux",
        "description": "Gera layouts em Tailwind CSS elegantes, responsivos e acessíveis com foco em dark mode.",
        "prompt": "Escreva código HTML/JSX com classes utilitárias do Tailwind CSS que crie um componente interativo moderno, utilizando cores frias e efeitos de blur de fundo (glassmorphism).",
    },
    {
        "title": "Commit Message Formatter",
        "category": "system",
        "description": "Gera mensagens de commit seguindo a especificação de Conventional Commits.",
        "prompt": "Com base nas alterações de código fornecidas, gere uma mensagem de commit curta e sem ambiguidades no formato Conventional Commits (ex: feat(ui): add collapse button).",
    },
]


@router.get("", response_model=list[PromptResponse])
async def list_prompts(session: AsyncSession = Depends(get_session)):
    logger.info("[start] list_prompts")
    result = await session.execute(select(Prompt))
    prompts = result.scalars().all()

    if not prompts:
        # Seeding
        logger.info("[prompts] table is empty, seeding default prompts")
        for item in INITIAL_PROMPTS:
            new_p = Prompt(
                id=uuid.uuid4(),
                title=item["title"],
                category=item["category"],
                prompt=item["prompt"],
                description=item["description"],
            )
            session.add(new_p)
        await session.commit()

        result = await session.execute(select(Prompt))
        prompts = result.scalars().all()

    return [
        PromptResponse(
            id=str(p.id),
            title=p.title,
            category=p.category,
            prompt=p.prompt,
            description=p.description,
        )
        for p in prompts
    ]


@router.post("", response_model=PromptResponse, status_code=status.HTTP_201_CREATED)
async def create_prompt(
    body: PromptSchema, session: AsyncSession = Depends(get_session)
):
    logger.info(f"[start] create_prompt: {body.title}")
    new_p = Prompt(
        id=uuid.uuid4(),
        title=body.title,
        category=body.category,
        prompt=body.prompt,
        description=body.description,
    )
    session.add(new_p)
    await session.commit()
    return PromptResponse(
        id=str(new_p.id),
        title=new_p.title,
        category=new_p.category,
        prompt=new_p.prompt,
        description=new_p.description,
    )


@router.put("/{prompt_id}", response_model=PromptResponse)
async def update_prompt(
    prompt_id: str,
    body: PromptSchema,
    session: AsyncSession = Depends(get_session),
):
    logger.info(f"[start] update_prompt: {prompt_id}")
    try:
        pid = uuid.UUID(prompt_id)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid prompt UUID"
        )

    p = await session.get(Prompt, pid)
    if not p:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Prompt not found"
        )

    p.title = body.title
    p.category = body.category
    p.prompt = body.prompt
    p.description = body.description

    await session.commit()
    return PromptResponse(
        id=str(p.id),
        title=p.title,
        category=p.category,
        prompt=p.prompt,
        description=p.description,
    )


@router.delete("/{prompt_id}")
async def delete_prompt(prompt_id: str, session: AsyncSession = Depends(get_session)):
    logger.info(f"[start] delete_prompt: {prompt_id}")
    try:
        pid = uuid.UUID(prompt_id)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid prompt UUID"
        )

    p = await session.get(Prompt, pid)
    if not p:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Prompt not found"
        )

    await session.delete(p)
    await session.commit()
    return {"status": "deleted", "id": prompt_id}
