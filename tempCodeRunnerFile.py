    import os
    if not os.path.exists(csv_file):
        print("❌ Le fichier n'existe pas :", os.path.abspath(csv_file))
        sys.exit()