from layout import layout
from app_instance import app
import callbacks  # Import after app is defined

app.layout = layout

if __name__ == "__main__":
    app.run(debug=True)
