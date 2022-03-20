import re


def email_parse(email: str) -> dict:
    """
        Парсит переданную email-строку на атрибуты и возвращает словарь
        :param email: строковое входное значение обрабатываемого email
        :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
        """
    RE_MAIL = re.compile(r"^(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)$",
                         re.IGNORECASE | re.ASCII)
    pass
    msg = f'wrong email: {email}'
    match_email = RE_MAIL.match(email)
    if not match_email:
        raise ValueError(msg)
    dict_out = match_email.groupdict()
    return dict_out


if __name__ == '__main__':
    email_parse('someone@geekbrains.ru')
    email_parse('sometwo@geekbrains.ru')
    email_parse('someotree@geekbrainsru')
