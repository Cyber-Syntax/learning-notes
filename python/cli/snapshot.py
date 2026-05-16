from dataclasses import dataclass, field


@dataclass
class TransactionSnapshot:
    phase: str
    installed: list = field(default_factory=list)
    failed: list = field(default_factory=list)
    downloading: dict = field(default_factory=dict)


snapshot = TransactionSnapshot(phase="download")

snapshot.downloading["obsidian"] = 55

snapshot.installed.append("appflowy")


def render(snapshot):
    print(snapshot.phase)

    for pkg, progress in snapshot.downloading.items():
        print(pkg, progress)


print(render)
