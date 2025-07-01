#lesson 20 homework

import sqlite3
import pandas as pd

conn = sqlite3.connect(r"C:\Users\User\Desktop\Python lessons\Chinook_Sqlite.sqlite")

# Test: list tables again
tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table';", conn)
print(tables)
# Task 1: Customer Purchases Analysis

# Loading invoices and Customers

invoices = pd.read_sql("SELECT * FROM Invoice", conn)
customers = pd.read_sql("SELECT * FROM Customer", conn)

# Total spent per customer

total_spent = invoices.groupby("CustomerId")["Total"].sum().reset_index()

# Merge with customer names

customer_total = pd.merge(total_spent, customers, on="CustomerId")

# Select top 5

top_5_customers = customer_total.sort_values(by="Total", ascending=False).head(5)

# Display selected columns
top_5 = top_5_customers[["CustomerId", "FirstName", "LastName", "Total"]]

print("Top 5 customers by total purchase:")
print(top_5)

# Task 2: Album vs. Individual Track Purchases

import pandas as pd
import sqlite3

# Connecting to the database
conn = sqlite3.connect(r"C:\Users\User\Desktop\Python lessons\Chinook_Sqlite.sqlite")

# Loading tables
invoice = pd.read_sql("SELECT InvoiceId, CustomerId FROM Invoice", conn)
invoice_line = pd.read_sql("SELECT * FROM InvoiceLine", conn)
track = pd.read_sql("SELECT * FROM Track", conn)
album = pd.read_sql("SELECT * FROM Album", conn)

# Merge InvoiceLine with Invoice to get CustomerId
invoice_line = invoice_line.merge(invoice, on="InvoiceId", how="left")

# Merge InvoiceLine -> Track -> Album to get album for each purchase
invoice_album = invoice_line.merge(track[['TrackId', 'AlbumId']], on="TrackId", how="left")

# Count total tracks per album
album_track_counts = track.groupby("AlbumId")["TrackId"].count().reset_index()
album_track_counts.rename(columns={"TrackId": "AlbumTrackCount"}, inplace=True)

# Merge to get album's full track count
invoice_album = invoice_album.merge(album_track_counts, on="AlbumId", how="left")

# Count tracks purchased by customer per album
cust_album_purchase = invoice_album.groupby(["CustomerId", "AlbumId"]).agg(
    PurchasedTrackCount=('TrackId', 'count'),
    AlbumTrackCount=('AlbumTrackCount', 'first')
).reset_index()

# Determine if full album was purchased
cust_album_purchase["FullAlbum"] = cust_album_purchase["PurchasedTrackCount"] == cust_album_purchase["AlbumTrackCount"]

#  FIX 1: Add parentheses to .reset_index()
customer_album_pref = cust_album_purchase.groupby("CustomerId")["FullAlbum"].any().reset_index()

#  FIX 2: Rename column from boolean to label
customer_album_pref["Preference"] = customer_album_pref["FullAlbum"].apply(
    lambda x: "Full Album" if x else "Individual Tracks"
)

# Calculate percentages
summary = customer_album_pref["Preference"].value_counts(normalize=True) * 100
summary = summary.round(2).astype(str) + "%"

print("\n Customer album vs individual track preference:")
print(summary)
