import tempfile
import shutil
import os
import pytest

from utils.file_loader import read_files

@pytest.fixture
def test_dir():
    # 创建一个临时目录
    temp_dir = tempfile.mkdtemp()

    # 创建多个测试文件
    files = {
        "note1.md": "# Note 1\nContent of note 1",
        "note2.md": "# Note 2\nContent of note 2",
        "ignore.txt": "Should not be read",
        "subdir/note3.md": "# Note 3\nContent of note 3 in subdir"
    }

    for path, content in files.items():
        full_path = os.path.join(temp_dir, path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)

    yield temp_dir

    # 清理临时目录
    shutil.rmtree(temp_dir)


def test_read_md_files(test_dir):
    file_filter = lambda f: f.endswith('.md')
    notes = read_files(test_dir, file_filter)
    note_names = sorted([n['name'] for n in notes])

    expected_names = sorted([
        "note1.md",
        "note2.md",
        os.path.join("subdir", "note3.md")
    ])

    assert note_names == expected_names
    for note in notes:
        assert "# Note" in note["content"]


def test_ignore_non_md_files(test_dir):
    file_filter = lambda f: f.endswith('.md')
    notes = read_files(test_dir, file_filter)
    for note in notes:
        assert note["name"].endswith(".md")
