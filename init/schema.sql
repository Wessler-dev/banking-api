CREATE TABLE IF NOT EXISTS individual (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    monthly_income REAL,
    age INTEGER,
    full_name TEXT,
    phone_number INTEGER,
    email TEXT,
    category TEXT,
    balance REAL
);

CREATE TABLE IF NOT EXISTS legal_entity (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    revenue REAL,
    age INTEGER,
    trade_name TEXT,
    phone_number INTEGER,
    corporate_email TEXT,
    category TEXT,
    balance REAL
);

INSERT INTO
    individual (
        monthly_income,
        age,
        full_name,
        phone_number,
        email,
        category,
        balance
    )
VALUES (
        5000.00,
        35,
        'João da Silva',
        99998888,
        'joao@example.com',
        'Categoria A',
        10000.00
    ),
    (
        4000.00,
        45,
        'Maria Oliveira',
        77776666,
        'maria@example.com',
        'Categoria B',
        15000.00
    ),
    (
        6000.00,
        28,
        'Pedro Santos',
        55554444,
        'pedro@example.com',
        'Categoria C',
        8000.00
    );

INSERT INTO
    legal_entity (
        revenue,
        age,
        trade_name,
        phone_number,
        corporate_email,
        category,
        balance
    )
VALUES (
        100000.00,
        10,
        'Empresa XYZ',
        11112222,
        'contato@empresa.com',
        'Categoria A',
        50000.00
    ),
    (
        80000.00,
        5,
        'Empresa ABC',
        33334444,
        'contato@abc.com',
        'Categoria B',
        70000.00
    ),
    (
        120000.00,
        8,
        'Empresa 123',
        55556666,
        'contato@123.com',
        'Categoria C',
        90000.00
    );