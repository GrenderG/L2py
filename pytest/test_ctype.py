from common.ctype import ctype


def test_types():
    c_types = [eval(f"ctype.{i}") for i in dir(ctype) if i[0:2] != "__"]

    convert_dict = {"bool": (1, True),
                    "byte": (10000, 16)}

    for c_type_i in c_types[:2]:
        value = c_type_i(convert_dict[type_name := c_type_i.__name__][0])
        assert value == convert_dict[type_name][1]
