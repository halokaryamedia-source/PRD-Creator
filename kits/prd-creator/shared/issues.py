from __future__ import annotations

from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class Issue:
    code: str
    owner: str
    message: str
    path: str = ""
    line: int | None = None
    field: str = ""
    severity: str = "error"

    def as_dict(self) -> dict[str, object]:
        return {
            key: value
            for key, value in asdict(self).items()
            if value not in ("", None)
        }

    def __str__(self) -> str:
        location = self.path
        if self.line is not None:
            location = f"{location}:{self.line}" if location else f"line {self.line}"
        prefix = f"{self.code} [{self.owner}]"
        if location:
            prefix += f" {location}"
        if self.field:
            prefix += f" ({self.field})"
        return f"{prefix}: {self.message}"


class SourceParseError(ValueError):
    """A parser failure with stable machine code and exact source location."""

    def __init__(
        self,
        code: str,
        owner: str,
        message: str,
        *,
        path: str = "",
        line: int | None = None,
        field: str = "",
    ) -> None:
        self.issue = Issue(
            code=code,
            owner=owner,
            message=message,
            path=path,
            line=line,
            field=field,
        )
        super().__init__(str(self.issue))

    def as_issue(self) -> Issue:
        return self.issue
