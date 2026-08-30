# Security and Data Handling

PRD-Creator is publicly accessible but is not an appropriate storage location for private project/client production data.

## Do not commit

Do not commit or publish:

- credentials, API keys, tokens, passwords, or private configuration;
- private client/source files or material without explicit public-visibility approval;
- live project requirement registers, source inventories, canonical project work, or generated project deliveries when they contain non-public project information;
- personally identifying or confidential data not required by the public system repository;
- temporary transfer payloads, encoded stand-ins, or upload-only helper artifacts.

## Project packages

`workspace/active/<project>/` and `workspace/archive/<project>/` are local/external mount conventions. Project subdirectories are ignored by Git. Keep their actual project data in an authorized local/private repository or other approved storage location.

If a project must be used as a public example, create a deliberately sanitized example rather than publishing the live production package by default.

## Existing Git history

Deleting a file from the current tree or adding it to `.gitignore` does **not** remove copies already present in Git history.

If sensitive material is discovered in historical commits:

1. stop adding new copies;
2. determine whether the material is actually sensitive and whether credentials require rotation;
3. treat history rewriting, repository-visibility changes, and secret rotation as explicit security operations;
4. do not rewrite shared history as ordinary cleanup.

## Reporting

For a suspected exposure, contact the repository owner directly rather than opening a public issue containing the sensitive material.

## Scope

This policy covers repository data handling. Product/game content rights, third-party assets, trademarks, and libraries remain subject to their own licenses and permissions as stated in `LICENSE`.
