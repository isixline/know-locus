from core.parser import parse_links

def test_basic_links():
    content = "介绍 [[人工智能]] 和 [[深度学习]] 是关键。"
    result = parse_links(content)
    assert result == ["人工智能", "深度学习"]

def test_no_links():
    content = "这是没有链接的普通文本。"
    result = parse_links(content)
    assert result == []

def test_edge_cases():
    content = "[[重复]] 和 [[重复]] 应该都被提取。"
    result = parse_links(content)
    assert result == ["重复", "重复"]

def test_nested_brackets():
    content = "这不是链接 [[[链接]]。"
    result = parse_links(content)
    assert result == ["链接"]
