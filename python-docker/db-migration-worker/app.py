import sqlite3
import sys

class ClusterDatabaseManager:
    def __init__(self, db_file="cluster_state.db"):
        # Establish a connection to the SQLite database file
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
        self._initialize_tables()

    def _initialize_tables(self):
        """Enforce strict base relational schema definitions on startup."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS cluster_nodes (
                node_id INTEGER PRIMARY KEY AUTOINCREMENT,
                hostname TEXT UNIQUE NOT NULL,
                ip_address TEXT NOT NULL,
                cluster_role TEXT NOT NULL
            )
        """)
        self.connection.commit()

    def register_node(self, hostname, ip, role):
        """Insert infrastructure metrics securely using parameterized queries."""
        try:
            self.cursor.execute(
                "INSERT INTO cluster_nodes (hostname, ip_address, cluster_role) VALUES (?, ?, ?)",
                (hostname, ip, role)
            )
            self.connection.commit()
            print(f"💾 Node registration committed successfully: {hostname}")
        except sqlite3.IntegrityError:
            print(f"⚠️ Registration Conflict: Node '{hostname}' already exists in database infrastructure.")

    def fetch_inventory_manifest(self):
        """Query and display all logged relational records."""
        self.cursor.execute("SELECT * FROM cluster_nodes")
        records = self.cursor.fetchall()
        print("\n📋 Displaying Infrastructure Engine Inventory:")
        for record in records:
            print(f" - Node ID: {record[0]} | Host: {record[1]} | IP Mapping: {record[2]} | Role Profile: {record[3]}")

    def close(self):
        """Safely wind down database connections."""
        self.connection.close()

if __name__ == "__main__":
    print("=== Starting Relational Data Synchronization Engine ===\n")
    manager = ClusterDatabaseManager()
    
    # Execute database transactions simulating cluster node provisioning updates
    manager.register_node("k8s-control-plane-01", "10.0.1.10", "Master")
    manager.register_node("k8s-worker-node-01", "10.0.2.15", "Worker")
    manager.register_node("k8s-worker-node-02", "10.0.2.16", "Worker")
    
    # Intentionally trigger constraint validation to demonstrate error handling
    print("\n--- Testing Data Integrity / Constraint Handling ---")
    manager.register_node("k8s-worker-node-01", "10.0.2.15", "Worker")
    
    # Fetch final output manifest report
    manager.fetch_inventory_manifest()
    manager.close()
