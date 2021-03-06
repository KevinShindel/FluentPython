# аннотации функций
from inspect import signature


def clip(text: str, max_len: int = 80) -> str:
    ''' Return text clipped at the last space before or after max_len '''
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end_space = space_before
        else:
            space_after = text.rfind('', max_len)
            if space_after >=0:
                end = space_after
    if end is None: # no spaces found
        end = len(text)
    return text[:end].rstrip()


def main():
    annotations = clip.__annotations__  # содержит аннотации метода
    print(annotations)
    sig = signature(clip)
    print(sig.return_annotation)
    for param in sig.parameters.values():
        note = repr(param.annotation).ljust(13)
        print(note, ':', param.name, '=', param.default)


if __name__ == '__main__':
    main()
