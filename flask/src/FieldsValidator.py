import re
class FieldValidador():
    
    def ip_is_valid(self, ip):
        """
        Valida um endereço IP.

        Args:
            ip: O endereço IP a ser validado.

        Returns:
            True se o endereço IP for válido, False caso contrário.
        """

        regex = r"^((25[0-5]|2[0-4]\d|[01]?\d{1,2})\.){3}(25[0-5]|2[0-4]\d|[01]?\d{1,2})$"
        if not re.match(regex, ip):
            return False

        for octeto in ip.split("."):
            if not 0 <= int(octeto) <= 255:
                return False

        return True

    def is_not_null(sefl, x):
        x=x.strip()
        if x !='':
            return True
        else:
            False
    
