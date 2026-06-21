-- SDD-040 Schema
-- Migration 001: Core tables for Universal Orchestration Platform
-- This migration is idempotent (IF NOT EXISTS on all objects)

-- 1. models: decoupled model registry (avoids provider:model inline coupling)
CREATE TABLE IF NOT EXISTS models (
    id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL UNIQUE,
    provider_name VARCHAR(100) NOT NULL,
    context_window INTEGER DEFAULT 8192,
    cost_input DECIMAL(10,8) DEFAULT 0.0,
    cost_output DECIMAL(10,8) DEFAULT 0.0,
    capabilities TEXT[] NOT NULL DEFAULT '{}',
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- 2. capability_policies: per-capability provider/model preferences
CREATE TABLE IF NOT EXISTS capability_policies (
    id SERIAL PRIMARY KEY,
    capability VARCHAR(100) NOT NULL,
    priority_order INTEGER NOT NULL,
    model_id INTEGER NOT NULL REFERENCES models(id) ON DELETE CASCADE,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(capability, priority_order)
);

-- 3. provider_configs: provider connection settings
CREATE TABLE IF NOT EXISTS provider_configs (
    id SERIAL PRIMARY KEY,
    provider_type VARCHAR(50) NOT NULL,
    provider_name VARCHAR(100) NOT NULL,
    api_key TEXT,
    base_url TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    extra_config JSONB DEFAULT '{}',
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- 4. user_profiles: user preferences and settings
CREATE TABLE IF NOT EXISTS user_profiles (
    user_id VARCHAR(255) PRIMARY KEY,
    theme VARCHAR(50) DEFAULT 'dark',
    language VARCHAR(10) DEFAULT 'pt-BR',
    vault_path TEXT DEFAULT '',
    auto_update BOOLEAN DEFAULT TRUE,
    telemetry_enabled BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- 5. user_model_profiles: per-workflow model preferences
CREATE TABLE IF NOT EXISTS user_model_profiles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id VARCHAR(255) NOT NULL REFERENCES user_profiles(user_id) ON DELETE CASCADE,
    workflow_type VARCHAR(100) NOT NULL,
    model_name VARCHAR(200) NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(user_id, workflow_type)
);

-- 6. feature_flags: runtime feature toggles
CREATE TABLE IF NOT EXISTS feature_flags (
    flag VARCHAR(100) PRIMARY KEY,
    enabled BOOLEAN DEFAULT FALSE,
    description TEXT,
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- 7. failed_executions: dead letter queue for unprocessable requests
CREATE TABLE IF NOT EXISTS failed_executions (
    id UUID PRIMARY KEY,
    trace_id UUID,
    execution_id UUID,
    workflow VARCHAR(100),
    payload JSONB,
    error TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    reprocessed_at TIMESTAMPTZ
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_capability_policies_capability
    ON capability_policies(capability);
CREATE INDEX IF NOT EXISTS idx_provider_configs_type_name
    ON provider_configs(provider_type, provider_name);
CREATE INDEX IF NOT EXISTS idx_failed_executions_created
    ON failed_executions(created_at DESC);

-- Seed: default models
INSERT INTO models (name, provider_name, context_window, capabilities) VALUES
    ('qwen3:4b', 'ollama', 32768, '{fast_chat,tool_calling,rag}'),
    ('qwen3:14b', 'ollama', 32768, '{fast_chat,reasoning,tool_calling,rag}'),
    ('nomic-embed-text', 'ollama', 2048, '{rag}')
ON CONFLICT (name) DO NOTHING;

-- Seed: default capability policies
INSERT INTO capability_policies (capability, priority_order, model_id)
SELECT 'fast_chat', 0, id FROM models WHERE name = 'qwen3:4b'
UNION ALL
SELECT 'reasoning', 0, id FROM models WHERE name = 'qwen3:14b'
UNION ALL
SELECT 'rag', 0, id FROM models WHERE name = 'qwen3:14b'
UNION ALL
SELECT 'tool_calling', 0, id FROM models WHERE name = 'qwen3:4b'
ON CONFLICT DO NOTHING;

-- Seed: default feature flags
INSERT INTO feature_flags (flag, enabled, description) VALUES
    ('research_workflow', FALSE, 'Enable research workflow (multi-step deep research)'),
    ('coding_workflow', FALSE, 'Enable coding workflow (code generation/analysis)'),
    ('agent_mode', FALSE, 'Enable agent mode with extended tool access'),
    ('browser_use', FALSE, 'Enable browser automation capabilities'),
    ('multi_agent', FALSE, 'Enable multi-agent orchestration')
ON CONFLICT (flag) DO NOTHING;
