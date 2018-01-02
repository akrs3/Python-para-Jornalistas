{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import csv\n",
    "\n",
    "populacao = 0\n",
    "densidade = 0\n",
    "estado_desejado = input('Digite a sigla do estado: ')\n",
    "estado_desejado = estado_desejado.upper()\n",
    "\n",
    "arquivo = open('brasil.csv', encoding='utf8')\n",
    "\n",
    "for registro in csv.DictReader(arquivo):\n",
    "    if registro['estado'] == estado_desejado:\n",
    "        densidade = int(registro['habitantes']) / float(registro['area'])\n",
    "        municipio = registro[\"municipio\"]\n",
    "        #populacao += int(registro['habitantes']) # a = a + b / a+= b\n",
    "        print('Densidade de ' + str(municipio) + ' eh: ' +  str(densidade))\n",
    "\n",
    "#print('A populacao de ' + estado_desejado  + ' eh: ' + str(populacao))\n",
    "#print(f'A populacao de {estado_desejado} eh: {populacao}') NAO PEGOU\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import collections\n",
    "\n",
    "contador = collections.Counter()\n",
    "contador['PR'] += 1000\n",
    "contador['RJ'] += 1000"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import collections\n",
    "\n",
    "contador = collections.Counter()\n",
    "contador['PR'] += 1000\n",
    "contador['RJ'] += 1000\n",
    "print(contador)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.4.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
