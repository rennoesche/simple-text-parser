import re



def parser(sentences):

    def extract_name(sentences):
        re_name = r"(?P<name>\b[A-Z][a-z]+\b(?:\s[A-Z][a-z]+)+)"
        for sentence in sentences:
            match = re.search(re_name, sentence)
            if match:
                return match.group()
        return None

    def extract_phone(sentences):
        re_phone = r"(?:\+62|62|0)\d{10,11}"
        for sentence in sentences:
            match = re.search(re_phone, sentence)
            if match:
                return match.group()
        return None  
    
    def extract_email(sentences):
        re_email = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        for sentence in sentences:
            match = re.search(re_email, sentence)
            if match:
                return match.group()
        return None
    
    def extract_sekul(sentences):
        re_kampus = [
            r"Sekolah(?:\s[A-Z][a-z]+)+",
            r"Politeknik(?:\s[A-Z][a-z]+)",
            r"Universitas(?:\s[A-Z][a-z]+)"
        ]
        for re_ in re_kampus:
            for sentence in sentences:
                match = re.search(re_, sentence)
                if match:
                    return match.group()
            return None

    def extract_pend(sentences):
        re_pend = [
            r"Teknik(?:\s[A-Z][a-z]+)",
            r"Sistem(?:\s[A-Z][a-z]+)",
            r"Pendidikan(?:\s[A-Z][a-z]+)",
            r"Ilmu(?:\s[A-Z][a-z]+)",
            r"Rekayasa(?:\s[A-Z][a-z]+)",
            r"Administrasi(?:\s[A-Z][a-z]+)",
            r"Sastra(?:\s[A-Z][a-z]+)",
            r"Kedokteran(?:\s[A-Z][a-z]+)",
            r"Bahasa(?:\s[A-Z][a-z]+)"
        ]

        for sentence in sentences:
            for rp in re_pend:
                match = re.search(rp, sentence)
                if match:
                    return match.group()
        return None
    
    def extract_skill(sentences):
        skills = set()
        re_skill = r"skill\s*(.*?)(?=\n|$)"
        for sentence in sentences:
            sentence = sentence.replace('·', ',')
            match = re.findall(re_skill, sentence, re.IGNORECASE)
            for m in match:
                skills.update([skill.strip() for skill in m.split(',')])
        return list(skills)
    
    def extract_exp(sentences):
        exp_ = set()
        re_exp = r"pengalaman\s*(.*?)(\.)"
        for sentence in sentences:
            match = re.findall(re_exp, sentence, re.IGNORECASE)
            for ma in match:
                first_part = ma[0]
                exp_.update([exp.strip() for exp in first_part.split(',')])
        return list(exp_)
    

    data = {
        "nama": extract_name(sentences),
        "email": extract_email(sentences),
        "ponsel": extract_phone(sentences),
        "pengalaman": extract_exp(sentences),
        "pend_last": extract_sekul(sentences),
        "pendidikan": extract_pend(sentences),
        "skill": extract_skill(sentences)
    }

    return data