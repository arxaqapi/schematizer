import torch
from torch import nn

from schematizer.device import DEVICE

# L'état inital caché du décodeur est le vecteur
# obtenue à la sortie de l'encodeur
class S2SEncoder(nn.Module):
    def __init__(self,
                 input_size: int,
                 hidden_size: int,
                 ) -> None:
        """
        L'encoder prend en entrée une suite de mots formant une phrase
        et renvoie en sortie un vecteur unique représentant l'entrée.

        input_size: la taille d'entrée du vocabulaire
        hidden_size: la taille des états cachés du RNN
        num_layers: nombre de couce de RNN, Default = 1
        """
        super(S2SEncoder, self).__init__()
        self.hidden_size = hidden_size

        # L'entrée doit être transformée en un vecteur
        self.embedding = nn.Embedding(input_size, embedding_dim=hidden_size)
        self.gru = nn.GRU(input_size=hidden_size,
                          hidden_size=hidden_size)

    def initHidden(self):
        return torch.zeros(1, 1, self.hidden_size, device=DEVICE)

    def forward(self, input, hidden):
        embedded = self.embedding(input).view(1, 1, -1)
        output, hidden = self.gru(embedded, hidden)
        return output, hidden
