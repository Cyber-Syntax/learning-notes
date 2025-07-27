from typing import Any, TypedDict, cast

import orjson
import requests


class GitHubAsset(TypedDict):
    name: str
    size: int
    digest: str
    browser_download_url: str


class GitHubReleaseDetails(TypedDict):
    owner: str
    repo: str
    version: str
    prerelease: bool
    assets: list[GitHubAsset]


class GitHubReleaseFetcher:
    def __init__(self, owner: str, repo: str) -> None:
        self.owner: str = owner
        self.repo: str = repo
        self.api_url: str = f"https://api.github.com/repos/{owner}/{repo}/releases/latest"

    def fetch_latest_release(self) -> GitHubReleaseDetails:
        response: requests.Response = requests.get(self.api_url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(
                f"Failed to fetch the latest release. Status code: {response.status_code}"
            )

    def extract_asset_details(
        self, release_data: GitHubReleaseDetails
    ) -> GitHubReleaseDetails:
        return {
            "owner": self.owner,
            "repo": self.repo,
            "version": release_data.get("tag_name", ""),
            "prerelease": release_data.get("prerelease", False),
            "assets": self.filter_appimage_assets(
                cast(list[dict[str, Any]], release_data.get("assets", []))
            ),
        }

    def to_github_asset(self, asset: dict[str, Any]) -> GitHubAsset | None:
        try:
            return {
                "name": cast(str, asset.get("name")),
                "digest": cast(str, asset.get("digest")),
                "size": cast(int, asset.get("size")),
                "browser_download_url": cast(str, asset.get("browser_download_url")),
            }
        except (KeyError, TypeError):
            print("Failed to convert asset to GitHubAsset")
            return None

    def filter_appimage_assets(self, assets: list[dict[str, Any]]) -> list[GitHubAsset]:
        filtered_assets: list[GitHubAsset] = []
        
        for asset in assets:
            typed_asset = self.to_github_asset(asset)

            # Check if the asset is valid and ends with ".AppImage"
            if typed_asset and typed_asset["name"].endswith(".AppImage"):
                filtered_assets.append(typed_asset)

                checksum_variants: list[str] = [f"{typed_asset['name']}.sha256sum"]

                for variant in checksum_variants:
                    checksum_asset = next((a for a in assets if a.get("name") == variant), None)
                    typed_checksum = (
                        self.to_github_asset(checksum_asset) if checksum_asset else None
                    )
                    if typed_checksum:
                        filtered_assets.append(typed_checksum)
                    else:
                        print("Failed to convert checksum asset to GitHubAsset")

        return filtered_assets

    def write_to_file(self, data: GitHubReleaseDetails, file_name: str) -> None:
        with open(file_name, "wb") as file:
            file.write(orjson.dumps(data, option=orjson.OPT_INDENT_2))


if __name__ == "__main__":
    owner = "pbek"
    repo = "qownnotes"
    output_file = "latest_release_details.json"

    fetcher: GitHubReleaseFetcher = GitHubReleaseFetcher(owner, repo)
    try:
        release_data: GitHubReleaseDetails = fetcher.fetch_latest_release()
        asset_details: GitHubReleaseDetails = fetcher.extract_asset_details(release_data)
        fetcher.write_to_file(asset_details, output_file)
        print(f"Asset details written to {output_file}")
    except Exception as e:
        print(str(e))
