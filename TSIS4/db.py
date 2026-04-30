import psycopg2

class Database:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                dbname="snake_db",
                user="postgres",
                password="1555", 
                host="localhost"
            )
            self.cursor = self.conn.cursor()
            self._create_tables()
        except Exception as e:
            print(f"Database Error: {e}")

    def _create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS players (
                id SERIAL PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL
            );
            CREATE TABLE IF NOT EXISTS game_sessions (
                id SERIAL PRIMARY KEY,
                player_id INTEGER REFERENCES players(id),
                score INTEGER NOT NULL,
                level_reached INTEGER NOT NULL,
                played_at TIMESTAMP DEFAULT NOW()
            );
        """)
        self.conn.commit()

    def get_or_create_player(self, username):
        self.cursor.execute("INSERT INTO players (username) VALUES (%s) ON CONFLICT (username) DO NOTHING", (username,))
        self.cursor.execute("SELECT id FROM players WHERE username = %s", (username,))
        self.conn.commit()
        return self.cursor.fetchone()[0]

    def save_session(self, player_id, score, level):
        self.cursor.execute("INSERT INTO game_sessions (player_id, score, level_reached) VALUES (%s, %s, %s)", 
                           (player_id, score, level))
        self.conn.commit()

    def get_leaderboard(self):
        self.cursor.execute("""
            SELECT p.username, gs.score, gs.level_reached, gs.played_at 
            FROM game_sessions gs JOIN players p ON gs.player_id = p.id
            ORDER BY gs.score DESC LIMIT 10
        """)
        return self.cursor.fetchall()

    def get_personal_best(self, player_id):
        self.cursor.execute("SELECT MAX(score) FROM game_sessions WHERE player_id = %s", (player_id,))
        res = self.cursor.fetchone()[0]
        return res if res else 0