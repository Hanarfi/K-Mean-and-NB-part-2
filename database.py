# ==========================================================
# DATABASE SQLITE
# Sistem Analisis Data Pasien Rawat Inap Anak
# ==========================================================
import hashlib
import sqlite3
from config import DATABASE_NAME


def get_connection():
    """
    Membuat koneksi ke database SQLite.
    """
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def create_tables():
    """
    Membuat seluruh tabel database jika belum ada.
    """

    conn = get_connection()
    cursor = conn.cursor()

    # ======================================================
    # TABEL USERS
    # ======================================================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id_user INTEGER PRIMARY KEY AUTOINCREMENT,
        nama TEXT NOT NULL,
        username TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL,
        tanggal_dibuat TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # ======================================================
    # TABEL DATASET
    # ======================================================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS dataset (
        id_dataset INTEGER PRIMARY KEY AUTOINCREMENT,
        id_user INTEGER,
        nama_dataset TEXT NOT NULL,
        nama_file TEXT NOT NULL,
        jumlah_data INTEGER,
        status TEXT,
        tanggal_upload TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

        FOREIGN KEY(id_user)
        REFERENCES users(id_user)
    )
    """)

    # ======================================================
    # TABEL DATA PASIEN
    # ======================================================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS data_pasien (
        id_pasien INTEGER PRIMARY KEY AUTOINCREMENT,
        id_dataset INTEGER,

        no_rekam_medis TEXT,
        jk TEXT,
        ld TEXT,
        kelas_rawatan TEXT,
        usia TEXT,
        cara_keluar TEXT,
        ruang_rawat TEXT,
        diagnosa_utama TEXT,

        FOREIGN KEY(id_dataset)
        REFERENCES dataset(id_dataset)
    )
    """)

    # ======================================================
    # TABEL ANALISIS
    # ======================================================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS analisis (
        id_analisis INTEGER PRIMARY KEY AUTOINCREMENT,

        id_dataset INTEGER,
        id_pasien INTEGER,

        cluster_kmeans INTEGER,
        cluster_nb INTEGER,

        status TEXT,
        jarak REAL,

        tanggal TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

        FOREIGN KEY(id_dataset)
        REFERENCES dataset(id_dataset),

        FOREIGN KEY(id_pasien)
        REFERENCES data_pasien(id_pasien)
    )
    """)

    # ======================================================
    # TABEL EVALUASI MODEL
    # ======================================================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS evaluasi_model (

        id_evaluasi INTEGER PRIMARY KEY AUTOINCREMENT,

        id_dataset INTEGER,

        accuracy REAL,
        precision REAL,
        recall REAL,
        f1_score REAL,

        silhouette_score REAL,
        davies_bouldin REAL,

        cross_validation REAL,

        tanggal TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

        FOREIGN KEY(id_dataset)
        REFERENCES dataset(id_dataset)
    )
    """)

    # ======================================================
    # TABEL RIWAYAT
    # ======================================================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS riwayat (

        id_riwayat INTEGER PRIMARY KEY AUTOINCREMENT,

        id_dataset INTEGER,
        id_user INTEGER,

        jenis_analisis TEXT,
        keterangan TEXT,

        tanggal TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

        FOREIGN KEY(id_dataset)
        REFERENCES dataset(id_dataset),

        FOREIGN KEY(id_user)
        REFERENCES users(id_user)
    )
    """)

    # ======================================================
    # TABEL LOG AKTIVITAS
    # ======================================================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS log_aktivitas (

        id_log INTEGER PRIMARY KEY AUTOINCREMENT,

        id_user INTEGER,

        aktivitas TEXT,

        waktu TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

        FOREIGN KEY(id_user)
        REFERENCES users(id_user)
    )
    """)

    conn.commit()
    conn.close()

    print("Database berhasil dibuat.")

# ==========================================================
# MEMBUAT ADMIN DEFAULT
# ==========================================================

def create_default_admin():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM users
        WHERE username=?
    """, ("admin",))

    admin = cursor.fetchone()

    if admin is None:

        password = hashlib.sha256(
            "admin123".encode()
        ).hexdigest()

        cursor.execute("""
            INSERT INTO users
            (
                nama,
                username,
                email,
                password,
                role
            )
            VALUES
            (?, ?, ?, ?, ?)
        """, (

            "Administrator",

            "admin",

            "admin@gmail.com",

            password,

            "Admin"

        ))

        conn.commit()

    conn.close()


# ==========================================================
# FUNGSI DASAR DATABASE
# ==========================================================

def execute_query(query, params=()):
    """
    Menjalankan query INSERT, UPDATE, DELETE.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(query, params)

    conn.commit()
    conn.close()


def fetch_one(query, params=()):
    """
    Mengambil satu data.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(query, params)

    data = cursor.fetchone()

    conn.close()

    return data


def fetch_all(query, params=()):
    """
    Mengambil banyak data.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(query, params)

    data = cursor.fetchall()

    conn.close()

    return data


def insert(table, data):
    """
    Menambahkan data ke database.
    """

    columns = ", ".join(data.keys())
    placeholders = ", ".join(["?"] * len(data))

    query = f"""
        INSERT INTO {table}
        ({columns})
        VALUES
        ({placeholders})
    """

    execute_query(query, tuple(data.values()))


def update(table, data, condition, params):
    """
    Mengubah data.
    """

    columns = ", ".join([f"{key}=?" for key in data.keys()])

    query = f"""
        UPDATE {table}
        SET {columns}
        WHERE {condition}
    """

    execute_query(
        query,
        tuple(data.values()) + tuple(params)
    )


def delete(table, condition, params):
    """
    Menghapus data.
    """

    query = f"""
        DELETE FROM {table}
        WHERE {condition}
    """

    execute_query(query, params)
