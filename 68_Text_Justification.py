class Solution(object):
    """
    1. round robin
    2. corner case when len(cur_words) == 1
    3. ljust
    """
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        r_lines, cur_words, cur_len = [], [], 0
        for w in words:
            if cur_len + len(w) + len(cur_words) > maxWidth:
                for i in range(maxWidth - cur_len):
                    cur_words[i % ((len(cur_words) - 1) or 1)] += " "
                r_lines.append("".join(cur_words))
                cur_words, cur_len = [], 0
            cur_words.append(w)
            cur_len += len(w)
        r_lines.append(" ".join(cur_words).ljust(maxWidth))
        return r_lines
