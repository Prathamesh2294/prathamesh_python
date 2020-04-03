{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Sales Report"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### DATA EXTRACTION"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import os"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [],
   "source": [
    "orders = pd.read_csv(\".//orders_data.csv\")\n",
    "new_df=pd.DataFrame()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### DATA PROCESSING(Merging Multiple Files in to One csv file)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "complete_sales.csv\n",
      "December_sales.csv\n",
      "February_sales.csv\n",
      "January_sales.csv\n"
     ]
    }
   ],
   "source": [
    "files=[file for file in os.listdir(\"C:\\\\Program Files\\\\Python36\\\\suven\\\\Notebooks\")]\n",
    "for file in files:\n",
    "    if(file.endswith('sales.csv')):\n",
    "        print(file)\n",
    "        df=pd.read_csv(\"C:\\\\Program Files\\\\Python36\\\\suven\\\\Notebooks\\\\\"+file)\n",
    "        new_df=pd.concat([new_df,df])\n",
    "new_df.to_csv(\"complete_sales.csv\",index=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
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
   "version": "3.6.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
