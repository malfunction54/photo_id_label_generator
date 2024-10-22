import inkex
import shortuuid

class IdGenerator(inkex.TextExtension):
    # dict to hold label to UUID associations
    ids = {}
    # by default, restrict values to numeric
    idGen = shortuuid.ShortUUID(alphabet="0123456789")

    def process_chardata(self, text):
        if "{{" in text and "}}" in text:
            # assume only a single occurence of a replacement
            # in a single text element
            prefix = text.split("{{")[0]
            remainder = text.split("{{")[-1]
            placeholder = remainder.split("}}")[0]
            postfix = remainder.split("}}")[-1]
            if placeholder not in self.ids:
                new_id = self.idGen.random(length=10)
                self.ids[placeholder] = new_id
            return prefix + self.ids[placeholder] + postfix
        else:
            # return unmodified text
            return text

IdGenerator().run()
