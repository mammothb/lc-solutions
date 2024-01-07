import string
from typing import Dict


class Codec:
    n_chars = 62
    chars = string.ascii_letters + string.digits
    prefix = "http://tinyurl.com/"
    index = 0
    long_to_id: Dict[str, int] = {}
    id_to_long: Dict[int, str] = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        if longUrl in self.long_to_id:
            id = self.long_to_id[longUrl]
        else:
            id = self.index
            self.long_to_id[longUrl] = self.index
            self.id_to_long[self.index] = longUrl
            self.index += 1

        short_url = ""
        while id > 0:
            short_url += self.chars[id % self.n_chars]
            id //= 62

        return f"{self.prefix}{short_url[::-1]}"

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        short_url = shortUrl[len(self.prefix) :]
        id = 0
        for c in short_url:
            ord_c = ord(c)
            if ord("a") <= ord_c <= ord("z"):
                id = id * self.n_chars + ord_c - ord("a")
            elif ord("A") <= ord_c <= ord("Z"):
                id = id * self.n_chars + ord_c - ord("A") + 26
            else:
                id = id * self.n_chars + ord_c - ord("0") + 52
        return self.id_to_long[id]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
