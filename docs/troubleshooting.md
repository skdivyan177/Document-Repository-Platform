# Troubleshooting

## Docker Image Download Issue
I encountered a persistent EOF (end of file) error while pulling Docker images. Resolved through Docker Desktop configuration and network troubleshooting, also had to mess around with my laptop proxy settings.

## SQLite Database Path Issue
Accidentally created an empty database by running commands from the wrong directory (higher up in the repository instead of in the api folder). Resolved by connecting to the correct database file, and deleting the file higher up in the repository.

## SQL Insert Error
Metadata insertion failed due to malformed SQL syntax. I had to look through the error logs and correct the query.