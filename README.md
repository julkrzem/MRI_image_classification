The aim of this project was to develop and test different types of neural networks in order to classify MRI images, and identify a type of tumor visible in the sample.

### Dataset and Preprocessing  

The dataset used for the project was downloaded from Kaggle: https://doi.org/10.34740/kaggle/dsv/2645886 and it consists of over 7000 brain scan images (6726 after removing duplicates) covering three main types of tumors:  
- Meningiomas (2) typically located near the outer surface of the skull.  
- Pituitary tumors (3) that develop centrally in the pituitary gland.  
- Gliomas (1) that arise from glial cells and can appear in different regions of the brain
As well as negative samples (no tumor image).

When training a model on images there is sometimes a risk that it can unintentionally learn patterns unrelated to the actual disease, based on some artifacts present in the image such as doctor annotations, differences in imaging equipment, or medical apparatus rather than identifying the biological characteristics

To maintain consistency and reduce potential biases, a universal PyTorch dataset was created and preprocessed which included:
- Cropping, adjusting brightness, and resizing the images
- Converting images to grayscale
- Saving the processed images

### Model Development

To find the most effective model, multiple approaches were tested step by step:
- Baseline model - the initial network architecture was based on PyTorch tutorial on training an image classifier
- Custom CNN - a convolutional neural network (CNN) was designed
- Transfer learning - a pre-trained model was used with adjusted linear layer
- EfficientNet-based model -the initial layers of EfficientNet were used with new convolutional layers that were trained
- Data augmentation on custom CNN - CNN was trained on an augmented dataset

### Results

After evaluating all models, the best-performing approach was selected (Custom CNN with data augmentation). In a final test it was also used for binary classification (tumor vs. no tumor) achieving high results, which confirmed the model’s reliability

## Info

*The project was developed for educational purpose only.*
*Some parts of notebooks in this project were based on or inspired by the PyTorch Tutorials (https://pytorch.org/tutorials)*

*DISCLAIMER: This code and analysis are provided "as-is" without warranty of any kind, either express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, or non-infringement. The author makes no representations regarding the accuracy, completeness, or validity of any data, analysis, or conclusions contained herein. The user acknowledges that they should verify any conclusions or results independently before making decisions based on this content. The author shall not be liable for any damages, including but not limited to direct, indirect, incidental, special, or consequential damages, or any loss of profit, data, or use, arising from the use or inability to use this code and analysis.*