# Security Policy

## Supported Scope

This repository contains Markdown templates, examples, and a small validation script. It should not contain production credentials, customer data, payment records, or private consultation records.

## Please Do Not Commit

- API keys or tokens
- `.env` files with real values
- Customer or client records
- Payment logs
- Private consultation notes
- Production URLs that should not be public
- Screenshots that expose private dashboards

## Reporting a Problem

If you find an accidental secret, private record, or unsafe workflow template, please open a GitHub issue with a brief description. Do not paste the secret or private content into the issue.

## Maintainer Checklist

Before accepting changes:

1. Confirm examples use fake data only.
2. Confirm no credentials or private records are included.
3. Run the template validator when template headings change.
4. Keep safety guidance practical and easy for non-engineers to follow.

