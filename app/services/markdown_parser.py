from markdown_it import MarkdownIt


def extract_markdown_blocks(content: str) -> list[dict]:
    tokens = MarkdownIt().parse(content)

    blocks = []
    heading_path = []
    list_depth = 0
    current_list = []

    i = 0

    while i < len(tokens):
        token = tokens[i]

        if token.type == "heading_open":
            inline_token = tokens[i + 1]
            heading = inline_token.content

            level = int(token.tag[1])
            heading_path = heading_path[:level - 1]
            heading_path.append(heading)

            i += 3
            continue

        if token.type == "paragraph_open":
            inline_token = tokens[i + 1]

            blocks.append({
                "content": inline_token.content,
                "block_type": "paragraph",
                "heading_path": heading_path.copy(),
            })

            i += 3
            continue

        if token.type in ("bullet_list_open", "ordered_list_open"):
            list_depth = 0
            list_items = []
            j = i

            while j < len(tokens):
                current = tokens[j]

                if current.type in ("bullet_list_open", "ordered_list_open"):
                    list_depth += 1

                elif current.type in ("bullet_list_close", "ordered_list_close"):
                    list_depth -= 1

                    if list_depth == 0:
                        break

                elif current.type == "inline":
                    indent = "  " * max(
                        0, (current.level - token.level - 2) // 2
                    )
                    list_items.append(f"{indent}- {current.content}")

                j += 1

            blocks.append({
                "content": "\n".join(list_items),
                "block_type": "list",
                "heading_path": heading_path.copy(),
            })

            i = j + 1
            continue

        if token.type == "inline" and list_depth > 0:
            current_list.append(token.content)
            i += 1
            continue

        if token.type == "fence":
            blocks.append({
                "content": token.content,
                "block_type": "code",
                "heading_path": heading_path.copy(),
            })

        i += 1

    return blocks