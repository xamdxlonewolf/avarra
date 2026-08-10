# Avarra

Worldbuilding notes and materials for Avarra.

## Cursor Cloud specific instructions

- This is currently a **documentation / worldbuilding repository**. As of this writing it contains only Markdown notes (e.g. `README.md`) — there is **no application code, no dependency manifest, no build system, and no automated tests/lint** to run. There is nothing to install; the environment update script is intentionally a no-op.
- Because there is no runnable application yet, there is no dev server, service, or "hello world" flow to exercise. If/when application code is added, update this section with how to install, build, run, lint, and test it.
- Database convention (from repo owner): the intended database is **Oracle**. If an `apex/` folder or a root APEX export SQL file (e.g. `f191.sql`, where the number is the APEX app id) appears, **do not modify those** — they are Oracle APEX exports. For new database objects, follow any existing table/view/PLSQL naming prefix/suffix already present; if none exists and no convention has been given, ask the owner (or consult an `oracle-db-skills-main` folder if provided) before creating objects.
