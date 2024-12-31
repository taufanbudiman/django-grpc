from django.conf import settings

from core.custom_hasher import CustomPBKDF2PasswordHasher


def validate_password_for_app(app_name, password, encoded_password):
    """
    Memvalidasi password dengan secret key yang sesuai dengan aplikasi yang sudah didaftarkan.

    app_name: Nama aplikasi yang digunakan untuk mencari secret key
    password: Password yang dimasukkan oleh pengguna
    encoded_password: Password yang sudah di-hash (disimpan di database)

    return: True jika password valid, False jika tidak
    """
    secret_key = settings.APP_SECRET_KEYS.get(app_name)

    if not secret_key:
        raise ValueError(f"Secret key untuk aplikasi {app_name} tidak ditemukan.")

    # Menggunakan CustomPBKDF2PasswordHasher dengan secret key yang sesuai
    hasher = CustomPBKDF2PasswordHasher()
    hasher.salt = lambda: secret_key

    return hasher.verify(password, encoded_password)
