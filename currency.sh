crncy() {
  local cmd=$1
  local amount=$2
  local currency_code=""

  if [[ $cmd == from* ]]; then
    python3 ~/bin/currency.py "$amount" 0 "${cmd#from}"
  elif [[ $cmd == to* ]]; then
    python3 ~/bin/currency.py "$amount" 1 "${cmd#to}"
  fi
}
