# Plan: Align Wiki with INSTRUCTIONS.md

## Objective
Update the `openwiki` directory to comply with the requirements specified in `/openwiki/INSTRUCTIONS.md`.

## Requirements Checklist
1. **Frontmatter Compliance**: All `.md` files in `openwiki/` must have the 12-field YAML frontmatter.
2. **Mirroring**: Ensure folder hierarchy reflects the structure of `src/`.
3. **Module Documentation**: Every source module needs an OKF page in `openwiki/modules/`.
4. **ISO Classification**: Proper labeling with `iso_doc_type` and `iso_viewpoint`.

## Tasks
1.  **Audit existing files**: Scan all `.md` files in `/openwiki/` for frontmatter compliance.
2.  **Fix Frontmats**: Update any missing or incomplete frontmats in:
    - `quickstart.md`
    - `source_map.md`
    - `infrastructure.md`
    - Files in `modules/`
3.  **Directory Alignment**: Check if the directory structure (architecture, infrastructure, operations) matches the primary logical domains of the project and if the nested folders correctly group source components.
4.  **Module Expansion**: Verify that all subpackages under `src/autogen_team/` have corresponding entries in `openwiki/modules/`.

## Identified Items for Fixes
- `quickstart.md`: Add missing frontmatter.
- `source_map.md`: Add missing frontmatter.
- `infrastructure.md`: Add missing frontmatter.
- `modules/*`: Ensure consistent frontmats and coverage of core, application, infrastructure components.

## Backlog
- [ ] Detailed inspection of sub-components in `src/autogen_team/data_access` to see if additional wiki pages are needed.
- [ ] Audit internal links within the documentation for consistency.
