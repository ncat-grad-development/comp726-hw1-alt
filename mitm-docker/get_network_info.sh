#!/bin/bash

cat network_glif

echo "💀 Attacker IP: $(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' attacker)";
echo "💀 Attacker MAC: $(docker inspect -f '{{range .NetworkSettings.Networks}}{{.MacAddress}}{{end}}' attacker)";
echo "------------------------"
echo "🎯 Victim IP: $(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' victim)";
echo "🎯 Victim MAC: $(docker inspect -f '{{range .NetworkSettings.Networks}}{{.MacAddress}}{{end}}' victim)";
echo "------------------------"
echo "🌐 Gateway IP: $(docker inspect -f '{{range .NetworkSettings.Networks}}{{.Gateway}}{{end}}' attacker)";

# List of 9 quotes with the person's name appended
quotes=(
  "The hacker mind set doesn't actually see what happens on the other side, to the victim. - Kevin Mitnick"
  "The people who are crazy enough to think they can change the world are the ones who do. - Steve Jobs"
  "Stay hungry, stay foolish. - Steve Jobs"
  "Information is power. But like all power, there are those who want to keep it for themselves. - Aaron Swartz"
  "Hacking involves a different way of looking at problems that no one's thought of. - Walter O'Brien"
  "I am not a hacker, I am a security consultant. - Kevin Mitnick"
  "If you control the code, you control the world. - Marc Andreessen"
  "The real danger is not that computers will begin to think like men, but that men will begin to think like computers. - Sydney J. Harris"
  "Hackers are today's explorers. - Katie Hafner"
)

# Function to handle text-to-speech
speak() {
  local message=$1

  if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    if command -v espeak &> /dev/null; then
      espeak "$message"
    else
      echo "espeak not found. Please install it: sudo apt install espeak"
    fi

  elif [[ "$OSTYPE" == "darwin"* ]]; then
    if command -v say &> /dev/null; then
      say "$message"
    else
      echo "say command not found."
    fi

  elif [[ "$OSTYPE" == "cygwin" ]] || [[ "$OSTYPE" == "msys" ]]; then
    powershell.exe -Command "Add-Type –AssemblyName System.speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('$message');"
  else
    echo "Unsupported OS: $OSTYPE"
  fi
}

# Pick a random quote from the list
random_quote=${quotes[$RANDOM % ${#quotes[@]}]}

# Speak the random quote
speak "$random_quote"

# Final statement after the quote
speak "Keep the network info for the next steps. Good luck!"
