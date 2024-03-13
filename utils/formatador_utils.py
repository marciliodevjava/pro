class FormatadorDados:
    @classmethod
    def formatar_cpf(cls, cpf):
        cpf = cpf.replace(".", "").replace("-", "").strip()
        return cpf

    @classmethod
    def formatar_rg(cls, rg):
        rg = rg.replace(".", "").replace("-", "").replace(" ", "").strip()
        return rg

    @classmethod
    def formatador_nome(cls, nome):
        nome = nome.strip().title()
        return nome

    @classmethod
    def formatador_email(cls, email):
        return email.strip()
