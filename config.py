# ==========================================================
# CONFIGURASI APLIKASI
# Sistem Analisis Data Pasien Rawat Inap Anak
# ==========================================================

import os

# ==========================================================
# IDENTITAS APLIKASI
# ==========================================================

APP_NAME = "Sistem Analisis Data Pasien Rawat Inap Anak"
APP_SHORT_NAME = "SADPRIA"

HOSPITAL_NAME = "Kemenkes RS M. Djamil Padang"

APP_VERSION = "1.0"

# ==========================================================
# DATABASE
# ==========================================================

DATABASE_NAME = "database.db"

# ==========================================================
# METODE DATA MINING
# ==========================================================

JUMLAH_CLUSTER = 3

RANDOM_STATE = 42

TEST_SIZE = 0.20

CV_FOLD = 5

# ==========================================================
# ROLE USER
# ==========================================================

ROLE_ADMIN = "Admin"
ROLE_USER = "User"
ROLE_PIMPINAN = "Pimpinan"

ROLE_LIST = [
    ROLE_ADMIN,
    ROLE_USER,
    ROLE_PIMPINAN
]

# ==========================================================
# FOLDER
# ==========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

EXPORT_FOLDER = os.path.join(BASE_DIR, "exports")

ASSET_FOLDER = os.path.join(BASE_DIR, "assets")

# ==========================================================
# FILE ASSET
# ==========================================================

LOGO = os.path.join(ASSET_FOLDER, "logo.png")

BACKGROUND = os.path.join(ASSET_FOLDER, "background.jpg")

# ==========================================================
# FORMAT FILE
# ==========================================================

ALLOWED_EXTENSIONS = [
    "xlsx",
    "xls"
]

# ==========================================================
# TEMA
# ==========================================================

PRIMARY_COLOR = "#2563EB"

SECONDARY_COLOR = "#06B6D4"

SUCCESS_COLOR = "#22C55E"

WARNING_COLOR = "#F59E0B"

DANGER_COLOR = "#EF4444"

BACKGROUND_COLOR = "#F8FAFC"

CARD_COLOR = "#FFFFFF"

TEXT_COLOR = "#1F2937"

# ==========================================================
# STATUS ANALISIS
# ==========================================================

STATUS_TETAP = "Tetap"

STATUS_BERUBAH = "Berubah"
