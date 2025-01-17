from dataclasses import dataclass, field

from common.ctype import ctype
from common.document import Document


@dataclass(kw_only=True)
class SystemMessage(Document):
    __collection__: str = field(default="game_servers", repr=False, init=False)
    __database__: str = field(default="l2py", repr=False, init=False)

    text: ctype.int32
