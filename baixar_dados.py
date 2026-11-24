"""Baixa o CSV oficial do Stack Overflow Developer Survey 2025 e confere o checksum SHA-256.

Uso:  python baixar_dados.py
O arquivo (~141 MB) é salvo em dados/brutos/results.csv. Ele não vai para o GitHub
(limite de 100 MB por arquivo), por isso está no .gitignore.
"""
import hashlib
import urllib.request
from pathlib import Path

URL = "https://github.com/StackExchange/Survey/raw/refs/heads/main/packages/archive/2025/results.csv"
SHA256 = "2d1f65308877282edfb4470520eabbc08cb499118432a3dcec6a66c086aa2baa"
DESTINO = Path(__file__).parent / "dados" / "brutos" / "results.csv"


def sha256(caminho: Path) -> str:
    h = hashlib.sha256()
    with open(caminho, "rb") as f:
        for bloco in iter(lambda: f.read(1 << 20), b""):
            h.update(bloco)
    return h.hexdigest()


def main() -> None:
    DESTINO.parent.mkdir(parents=True, exist_ok=True)
    if not DESTINO.exists():
        print(f"Baixando {URL} ...")
        urllib.request.urlretrieve(URL, DESTINO)
    obtido = sha256(DESTINO)
    if obtido != SHA256:
        raise SystemExit(f"Checksum diferente do oficial!\n  esperado: {SHA256}\n  obtido:   {obtido}")
    print(f"OK: {DESTINO} ({DESTINO.stat().st_size / 1e6:.1f} MB), checksum confere com o oficial.")


if __name__ == "__main__":
    main()
