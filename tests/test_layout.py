from pathlib import Path


def test_scripts_exist():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "generate.py").is_file()
    assert (root / "scripts" / "land.py").is_file()
    assert (root / "docker-compose.yml").is_file()
