from model.utils import load_checkpoint
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    checkpoint = '../data/model/decoder/model5678epoch39'
    last_epoch, model_dict, optim_dict, valid_loss, train_loss, bleu_score = load_checkpoint(checkpoint)
    epochs = range(1, len(train_loss) + 1)

    fig, ax1 = plt.subplots()

    ax1.set_xlabel('Epoch')
    ax1.set_ylabel('Training Loss')
    ax1.plot(epochs, train_loss, color='tab:red', label='Loss')

    ax2 = ax1.twinx()

    ax2.set_ylabel('Bleu Score')
    ax2.plot(epochs, bleu_score, '--', color='tab:blue', label='BLEU')
    print(bleu_score)
    print(np.argmax(bleu_score))
    print(np.max(bleu_score))
    ax2.scatter(np.argmax(bleu_score), np.max(bleu_score), color='none', edgecolor='yellow')

    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax2.legend(lines1 + lines2, labels1 + labels2, loc=0)

    fig.tight_layout()
    plt.show()