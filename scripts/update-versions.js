import fs from 'fs';
import path from 'path';

const version = process.argv[2];
if (!version) {
  console.error("Erro: Por favor, forneça o número da versão (ex: 2.1.0)");
  process.exit(1);
}

// Limpa qualquer caractere 'v' no início da string se houver (ex: v2.1.0 -> 2.1.0)
const cleanVersion = version.replace(/^v/, '');

// Utilitário para ler, modificar e reescrever arquivos JSON mantendo a formatação
function updateJson(relativeFilePath, updater) {
  const absolutePath = path.resolve(relativeFilePath);
  if (!fs.existsSync(absolutePath)) {
    console.warn(`Aviso: Arquivo não encontrado: ${absolutePath}`);
    return;
  }
  const content = JSON.parse(fs.readFileSync(absolutePath, 'utf8'));
  updater(content);
  fs.writeFileSync(absolutePath, JSON.stringify(content, null, 2) + '\n', 'utf8');
  console.log(`Atualizado JSON: ${relativeFilePath} -> ${cleanVersion}`);
}

// 1. Atualiza desktop/package.json
updateJson('desktop/package.json', (data) => {
  data.version = cleanVersion;
});

// 2. Atualiza desktop/src-tauri/tauri.conf.json
updateJson('desktop/src-tauri/tauri.conf.json', (data) => {
  data.version = cleanVersion;
});

// 3. Atualiza desktop/src-tauri/Cargo.toml
const cargoPath = path.resolve('desktop/src-tauri/Cargo.toml');
if (fs.existsSync(cargoPath)) {
  let cargoContent = fs.readFileSync(cargoPath, 'utf8');
  cargoContent = cargoContent.replace(/^version = "[^"]*"/m, `version = "${cleanVersion}"`);
  fs.writeFileSync(cargoPath, cargoContent, 'utf8');
  console.log(`Atualizado Cargo.toml: ${cargoPath} -> ${cleanVersion}`);
} else {
  console.warn(`Aviso: Cargo.toml não encontrado em ${cargoPath}`);
}

console.log(`Sincronização de versão concluída com sucesso para v${cleanVersion}!`);
