class Solution:

    def encode(self, strs: List[str]) -> str:
        output=""
        for string in strs:
            output += f"{len(string)}@{string}"

        print(output)
        return output

    def decode(self, s: str) -> List[str]:
        output = []
        current = ""

        while len(s) > 0:
            if s[0] != '@':
                current += s[0]
                s = s[1:]
                continue
            else:
                length = int(current)

                output.append(s[1:length+1])

                s = s[length+1:]

                current = ""

        return output
            
            
