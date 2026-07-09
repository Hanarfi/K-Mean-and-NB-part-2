# ==========================================================
# DATABASE SQLITE
# Sistem Analisis Data Pasien Rawat Inap Anak
# ==========================================================

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
