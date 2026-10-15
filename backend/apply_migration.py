#!/usr/bin/env python3
"""
Apply migration 005 manually via Supabase admin API
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

url = os.environ.get("NEXT_PUBLIC_SUPABASE_URL", "https://inepfihjoadvmblcapch.supabase.co")
service_role_key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")

if not service_role_key:
    print("Error: SUPABASE_SERVICE_ROLE_KEY not found in environment")
    print("Please set it in your .env file")
    sys.exit(1)

client: Client = create_client(url, service_role_key)

# Read migration SQL
with open("supabase/migrations/005_add_technical_analysis_fields.sql", "r") as f:
    sql = f.read()

print("Applying migration 005: Add technical analysis fields")
print("=" * 60)

# The SQL uses ALTER TABLE statements
# We need to execute this via the Supabase REST API
# Unfortunately, the client library doesn't support raw SQL execution directly
# So we'll need to use the underlying REST API

import requests

headers = {
    "apikey": service_role_key,
    "Authorization": f"Bearer {service_role_key}",
    "Content-Type": "application/json",
    "Prefer": "return=minimal"
}

# Execute SQL via /rpc endpoint with postgresql_query function
# This requires creating a function in Supabase first, which is a chicken-and-egg problem

# Alternative: Use the Supabase Management API
# For now, let's just indicate what needs to be done

print("\nMigration SQL:")
print(sql)
print("\n" + "=" * 60)
print("\nTo apply this migration:")
print("1. Go to https://app.supabase.com/project/inepfihjoadvmblcapch/sql")
print("2. Paste the SQL from supabase/migrations/005_add_technical_analysis_fields.sql")
print("3. Click 'Run' to execute")
print("\nAlternatively, run: npx supabase db push")
