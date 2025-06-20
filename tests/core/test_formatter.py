from core.formatter import remove_links, remove_blank_dash_lines

def test_remove_links():
    content = "这是一个链接 [[人工智能]] 和 [[深度学习]] 的例子。"
    result = remove_links(content)
    assert result == "这是一个链接  和  的例子。"

def test_remove_links_no_links():
    content = "这是没有链接的普通文本。"
    result = remove_links(content)
    assert result == "这是没有链接的普通文本。"

def test_remove_links_edge_cases():
    content = "[[重复]] 和 [[重复]] 应该都被移除。"
    result = remove_links(content)
    assert result == " 和  应该都被移除。"

def test_remove_links_nested_brackets():
    content = "这不是链接 [[[链接]]。"
    result = remove_links(content)
    assert result == "这不是链接 [。"

def test_remove_blank_dash_lines_basic():
    content = "这是第一行。\n- \n- 第二行。\n- \n第三行。"
    result = remove_blank_dash_lines(content)
    assert result == "这是第一行。\n- 第二行。\n第三行。"

def test_remove_blank_dash_lines_no_blank_lines():
    content = "这是第一行。\n- 第二行。\n第三行。"
    result = remove_blank_dash_lines(content)
    assert result == "这是第一行。\n- 第二行。\n第三行。"

def test_remove_blank_dash_lines_only_dashes():
    content = "- \n- \n- "
    result = remove_blank_dash_lines(content)
    assert result == ""