#!/bin/bash

# List of websites to visit
sites=(
  "https://www.amazon.com"
  "https://www.ncat.edu"
  "https://www.google.com"
  "https://www.instagram.com"
  "https://www.tiktok.com"
  "https://www.facebook.com"
  "https://www.twitter.com"
  "https://www.youtube.com"
  "https://www.reddit.com"
  "https://www.netflix.com"
    "https://www.amazon.com"
  "https://www.ncat.edu"
  "https://www.google.com"
  "https://www.instagram.com"
  "https://www.tiktok.com"
  "https://www.facebook.com"
  "https://www.twitter.com"
  "https://www.youtube.com"
  "https://www.reddit.com"
  "https://www.netflix.com"
    "https://www.amazon.com"
  "https://www.ncat.edu"
  "https://www.google.com"
  "https://www.instagram.com"
  "https://www.tiktok.com"
  "https://www.facebook.com"
  "https://www.twitter.com"
  "https://www.youtube.com"
  "https://www.reddit.com"
  "https://www.netflix.com"
    "https://www.amazon.com"
  "https://www.ncat.edu"
  "https://www.google.com"
  "https://www.instagram.com"
  "https://www.tiktok.com"
  "https://www.facebook.com"
  "https://www.twitter.com"
  "https://www.youtube.com"
  "https://www.reddit.com"
  "https://www.netflix.com"
)

# Loop through the websites and perform curl for each
for site in "${sites[@]}"; do
  echo "Navigating to $site..."
  curl -s -o /dev/null "$site"  # Send a HEAD request to avoid large content
  sleep 2  # Sleep for 5 seconds before the next request
done

echo "All websites visited."
