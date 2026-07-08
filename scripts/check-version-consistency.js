import fs from 'fs';
import path from 'path';

// 1. Read package.json
const packagePath = path.resolve('desktop/package.json');
if (!fs.existsSync(packagePath)) {
  console.error(`Erro: package.json não encontrado em ${packagePath}`);
  process.exit(1);
}
const packageJson = JSON.parse(fs.readFileSync(packagePath, 'utf8'));
const packageVersion = packageJson.version;

// 2. Read tauri.conf.json
const tauriConfPath = path.resolve('desktop/src-tauri/tauri.conf.json');
if (!fs.existsSync(tauriConfPath)) {
  console.error(`Erro: tauri.conf.json não encontrado em ${tauriConfPath}`);
  process.exit(1);
}
const tauriConf = JSON.parse(fs.readFileSync(tauriConfPath, 'utf8'));
const tauriVersion = tauriConf.version;

// 3. Read Cargo.toml version
const cargoPath = path.resolve('desktop/src-tauri/Cargo.toml');
if (!fs.existsSync(cargoPath)) {
  console.error(`Erro: Cargo.toml não encontrado em ${cargoPath}`);
  process.exit(1);
}
const cargoContent = fs.readFileSync(cargoPath, 'utf8');
const cargoMatch = cargoContent.match(/^version = "([^"]*)"/m);
if (!cargoMatch) {
  console.error("Erro: Não foi possível encontrar a declaração de version em Cargo.toml");
  process.exit(1);
}
const cargoVersion = cargoMatch[1];

console.log(`Versões encontradas:`);
console.log(`  desktop/package.json:         ${packageVersion}`);
console.log(`  desktop/src-tauri/tauri.conf: ${tauriVersion}`);
console.log(`  desktop/src-tauri/Cargo.toml: ${cargoVersion}`);

if (packageVersion !== tauriVersion) {
  console.error(`Erro: Versões inconsistentes encontradas!`);
  console.error(`  package.json possui a versão ${packageVersion}`);
  console.error(`  tauri.conf.json possui a versão ${tauriVersion}`);
  process.exit(1);
}

if (packageVersion !== cargoVersion) {
  console.error(`Erro: Versões inconsistentes encontradas!`);
  console.error(`  package.json possui a versão ${packageVersion}`);
  console.error(`  Cargo.toml possui a versão ${cargoVersion}`);
  process.exit(1);
}

console.log("Sucesso: Todas as versões de arquivos de configuração estão perfeitamente sincronizadas!");
process.exit(0);
