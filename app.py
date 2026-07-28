"""
File Handler Studio
A Streamlit UI wrapper around a simple CRUD-style file management tool
(Create / Read / Update / Delete).

Run with:
    streamlit run app.py
"""

import streamlit as st
from pathlib import Path
from datetime import datetime

# ----------------------------------------------------------------------
# Config
# ----------------------------------------------------------------------
st.set_page_config(
    page_title="File Handler Studio",
    page_icon="🗂️",
    layout="centered",
)

# All files created/managed by this app live in a sandboxed folder,
# so the app never touches unrelated files on your machine.
WORKDIR = Path("user_files")
WORKDIR.mkdir(exist_ok=True)


# ----------------------------------------------------------------------
# Styling
# ----------------------------------------------------------------------
st.markdown(
    """
    <style>
    .main-title {
        font-size: 2.1rem;
        font-weight: 700;
        margin-bottom: 0rem;
    }
    .subtitle {
        color: #8a8f98;
        font-size: 1rem;
        margin-bottom: 1.5rem;
    }
    .stButton>button {
        border-radius: 8px;
        font-weight: 600;
        padding: 0.5rem 1.2rem;
    }
    .file-card {
        padding: 0.6rem 1rem;
        border-radius: 8px;
        background-color: rgba(127,127,127,0.08);
        margin-bottom: 0.4rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="main-title">🗂️ File Handler Studio</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Create, read, update, and delete text files — all from a clean UI.</div>',
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------
# Sidebar: file browser
# ----------------------------------------------------------------------
with st.sidebar:
    st.header("📁 Files")
    files = sorted([f.name for f in WORKDIR.iterdir() if f.is_file()])
    if files:
        for f in files:
            size = (WORKDIR / f).stat().st_size
            st.markdown(
                f'<div class="file-card">📄 <b>{f}</b><br>'
                f'<small>{size} bytes</small></div>',
                unsafe_allow_html=True,
            )
    else:
        st.caption("No files yet. Create one to get started!")

    st.divider()
    st.caption(f"Working directory: `{WORKDIR.resolve()}`")

# ----------------------------------------------------------------------
# Tabs for each operation
# ----------------------------------------------------------------------
tab_create, tab_read, tab_update, tab_delete = st.tabs(
    ["➕ Create", "📖 Read", "✏️ Update", "🗑️ Delete"]
)

# ---------------- CREATE ----------------
with tab_create:
    st.subheader("Create a new file")
    name = st.text_input("File name", key="create_name", placeholder="notes.txt")
    data = st.text_area("File content", key="create_data", height=150)

    if st.button("Create File", key="create_btn"):
        if not name.strip():
            st.error("Please enter a file name.")
        else:
            path = WORKDIR / name
            if path.exists():
                st.error(f"⚠️ A file named **{name}** already exists.")
            else:
                try:
                    path.write_text(data)
                    st.success(f"✅ File **{name}** created successfully!")
                    st.rerun()
                except Exception as err:
                    st.error(f"An error occurred: {err}")

# ---------------- READ ----------------
with tab_read:
    st.subheader("Read a file")
    files = sorted([f.name for f in WORKDIR.iterdir() if f.is_file()])
    if not files:
        st.info("No files available to read yet.")
    else:
        name = st.selectbox("Choose a file", files, key="read_select")
        if st.button("Read File", key="read_btn"):
            path = WORKDIR / name
            try:
                content = path.read_text()
                st.text_area("File content", content, height=250, key="read_output")
            except Exception as err:
                st.error(f"An error occurred: {err}")

# ---------------- UPDATE ----------------
with tab_update:
    st.subheader("Update a file")
    files = sorted([f.name for f in WORKDIR.iterdir() if f.is_file()])
    if not files:
        st.info("No files available to update yet.")
    else:
        name = st.selectbox("Choose a file", files, key="update_select")
        operation = st.radio(
            "What would you like to do?",
            ["Rename", "Append content", "Overwrite content"],
            horizontal=True,
            key="update_op",
        )
        path = WORKDIR / name

        if operation == "Rename":
            new_name = st.text_input("New file name", key="rename_input")
            if st.button("Rename File", key="rename_btn"):
                new_path = WORKDIR / new_name
                if not new_name.strip():
                    st.error("Please enter a new file name.")
                elif new_path.exists():
                    st.error(f"⚠️ A file named **{new_name}** already exists.")
                else:
                    try:
                        path.rename(new_path)
                        st.success(f"✅ Renamed to **{new_name}** successfully!")
                        st.rerun()
                    except Exception as err:
                        st.error(f"An error occurred: {err}")

        elif operation == "Append content":
            data = st.text_area("Content to append", key="append_input", height=120)
            if st.button("Append", key="append_btn"):
                try:
                    with open(path, "a") as fs:
                        fs.write("\n" + data)
                    st.success(f"✅ Content appended to **{name}** successfully!")
                except Exception as err:
                    st.error(f"An error occurred: {err}")

        elif operation == "Overwrite content":
            data = st.text_area("New content (replaces everything)", key="overwrite_input", height=120)
            if st.button("Overwrite", key="overwrite_btn"):
                try:
                    path.write_text(data)
                    st.success(f"✅ **{name}** overwritten successfully!")
                except Exception as err:
                    st.error(f"An error occurred: {err}")

# ---------------- DELETE ----------------
with tab_delete:
    st.subheader("Delete a file")
    files = sorted([f.name for f in WORKDIR.iterdir() if f.is_file()])
    if not files:
        st.info("No files available to delete yet.")
    else:
        name = st.selectbox("Choose a file", files, key="delete_select")
        confirm = st.checkbox(f"I confirm I want to permanently delete **{name}**")
        if st.button("Delete File", key="delete_btn", disabled=not confirm):
            path = WORKDIR / name
            try:
                path.unlink()
                st.success(f"🗑️ **{name}** deleted successfully!")
                st.rerun()
            except Exception as err:
                st.error(f"An error occurred: {err}")

# ----------------------------------------------------------------------
# Footer
# ----------------------------------------------------------------------
st.divider()
st.caption(
    f"File Handler Studio · Built with Python & Streamlit · "
    f"{datetime.now().strftime('%Y-%m-%d')}"
)