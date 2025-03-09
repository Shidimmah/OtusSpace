-- Таблица для User Service
CREATE TABLE users (
    id UUID PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Таблицы для Game Service
CREATE TABLE games (
    id UUID PRIMARY KEY,
    status VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    finished_at TIMESTAMP
);

CREATE TABLE game_participants (
    game_id UUID REFERENCES games(id),
    user_id UUID REFERENCES users(id),
    score INTEGER,
    PRIMARY KEY (game_id, user_id)
);

-- Таблицы для Tournament Service
CREATE TABLE tournaments (
    id UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    status VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    finished_at TIMESTAMP
);

CREATE TABLE tournament_participants (
    tournament_id UUID REFERENCES tournaments(id),
    user_id UUID REFERENCES users(id),
    PRIMARY KEY (tournament_id, user_id)
);

-- Таблица для Notification Service
CREATE TABLE notifications (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Таблица для Agent Service
CREATE TABLE agents (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    code TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Таблица для Replay Service
CREATE TABLE replays (
    id UUID PRIMARY KEY,
    game_id UUID REFERENCES games(id),
    data JSONB NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Таблица для Rating Service
CREATE TABLE ratings (
    user_id UUID PRIMARY KEY REFERENCES users(id),
    score INTEGER NOT NULL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);