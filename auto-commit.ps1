param(
  [string]$RepoPath = "C:\Projetos\python-facil"
)

Write-Host "⌚ Observando $RepoPath (Ctrl+C para sair)."

while ($true) {
    git -C $RepoPath add -A | Out-Null
    git -C $RepoPath commit -m "auto: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')" *> $null
    if ($LASTEXITCODE -eq 0) {
        git -C $RepoPath push
        Write-Host "✔ commit+push em $(Get-Date -Format 'HH:mm:ss')"
    }
    Start-Sleep -Seconds 20
}
