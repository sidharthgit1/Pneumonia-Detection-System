
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf


list_c=["C:\\Newds_covid&pnemonia\\Chest_xray_image_dataset_covid_19_and_others\\Covid_19\\1.CXRCTThoraximagesofCOVID-19fromSingapore.pdf-000-fig1a.png","C:\\Newds_covid&pnemonia\\Chest_xray_image_dataset_covid_19_and_others\\Covid_19\\1.CXRCTThoraximagesofCOVID-19fromSingapore.pdf-000-fig1b.png","C:\\Newds_covid&pnemonia\\Chest_xray_image_dataset_covid_19_and_others\\Covid_19\\1.CXRCTThoraximagesofCOVID-19fromSingapore.pdf-001-fig2a.png","C:\\Newds_covid&pnemonia\\Chest_xray_image_dataset_covid_19_and_others\\Covid_19\\1.CXRCTThoraximagesofCOVID-19fromSingapore.pdf-001-fig2b.png","C:\\Newds_covid&pnemonia\\Chest_xray_image_dataset_covid_19_and_others\\Covid_19\\1.CXRCTThoraximagesofCOVID-19fromSingapore.pdf-002-fig3a.png","C:\\Newds_covid&pnemonia\\Chest_xray_image_dataset_covid_19_and_others\\Covid_19\\1.CXRCTThoraximagesofCOVID-19fromSingapore.pdf-002-fig3b.png","C:\\Newds_covid&pnemonia\\Chest_xray_image_dataset_covid_19_and_others\\Covid_19\\1.CXRCTThoraximagesofCOVID-19fromSingapore.pdf-003-fig4a.png","C:\\Newds_covid&pnemonia\\Chest_xray_image_dataset_covid_19_and_others\\Covid_19\\1.CXRCTThoraximagesofCOVID-19fromSingapore.pdf-003-fig4b.png","C:\\Newds_covid&pnemonia\\Chest_xray_image_dataset_covid_19_and_others\\Covid_19\\1B734A89-A1BF-49A8-A1D3-66FAFA4FAC5D.jpeg","C:\\Newds_covid&pnemonia\\Chest_xray_image_dataset_covid_19_and_others\\Covid_19\\1F6343EE-AFEC-4B7D-97F5-62797EE18767.jpeg","C:\\Newds_covid&pnemonia\\Chest_xray_image_dataset_covid_19_and_others\\Covid_19\\1F6343EE-AFEC-4B7D-97F5-62797EE18767.jpeg"]
list_n=["C:\\Newds_covid&pnemonia\\Chest_xray_image_dataset_covid_19_and_others\\PNEUMONIA\\person1_bacteria_1.jpeg","C:\\Newds_covid&pnemonia\\Chest_xray_image_dataset_covid_19_and_others\\NORMAL\\IM-0003-0001.jpeg","C:\\Newds_covid&pnemonia\\Chest_xray_image_dataset_covid_19_and_others\\NORMAL\\IM-0005-0001.jpeg","C:\\Newds_covid&pnemonia\\Chest_xray_image_dataset_covid_19_and_others\\NORMAL\\IM-0006-0001.jpeg","C:\\Newds_covid&pnemonia\\Chest_xray_image_dataset_covid_19_and_others\\NORMAL\\IM-0007-0001.jpeg","C:\\Newds_covid&pnemonia\\Chest_xray_image_dataset_covid_19_and_others\\NORMAL\\IM-0009-0001.jpeg","C:\\Newds_covid&pnemonia\\Chest_xray_image_dataset_covid_19_and_others\\NORMAL\\IM-0010-0001.jpeg","C:\\Newds_covid&pnemonia\\Chest_xray_image_dataset_covid_19_and_others\\NORMAL\\IM-0011-0001.jpeg","C:\\Newds_covid&pnemonia\\Chest_xray_image_dataset_covid_19_and_others\\NORMAL\\IM-0011-0001-0001.jpeg","C:\\Newds_covid&pnemonia\\Chest_xray_image_dataset_covid_19_and_others\\NORMAL\\IM-0011-0001-0002.jpeg"]
list_p=["C:\\Newds_covid&pnemonia\\Chest_xray_image_dataset_covid_19_and_others\\NORMAL\\IM-0001-0001.jpeg","C:\\Newds_covid&pnemonia\\Chest_xray_image_dataset_covid_19_and_others\\PNEUMONIA\\person1_bacteria_2.jpeg","C:\\Newds_covid&pnemonia\\Chest_xray_image_dataset_covid_19_and_others\\PNEUMONIA\\person1_virus_6.jpeg","C:\\Newds_covid&pnemonia\\Chest_xray_image_dataset_covid_19_and_others\\PNEUMONIA\\person1_virus_7.jpeg","C:\\Newds_covid&pnemonia\\Chest_xray_image_dataset_covid_19_and_others\\PNEUMONIA\\person1_virus_8.jpeg","C:\\Newds_covid&pnemonia\\Chest_xray_image_dataset_covid_19_and_others\\PNEUMONIA\person1_virus_9.jpeg","C:\\Newds_covid&pnemonia\\Chest_xray_image_dataset_covid_19_and_others\\PNEUMONIA\\person1_virus_11.jpeg","C:\\Newds_covid&pnemonia\\Chest_xray_image_dataset_covid_19_and_others\\PNEUMONIA\\person1_virus_12.jpeg","C:\\Newds_covid&pnemonia\\Chest_xray_image_dataset_covid_19_and_others\\PNEUMONIA\\person1_virus_13.jpeg","C:\\Newds_covid&pnemonia\\Chest_xray_image_dataset_covid_19_and_others\\PNEUMONIA\\person2_bacteria_3.jpeg"]


img=[]
labels=[]
pred=[]


label_lines = [line.rstrip() for line
               in tf.gfile.GFile("C:\\Users\\n8100\\PycharmProjects\\Pneumonia_detection\\myapp\\logsold\\output_labels.txt")]
with tf.gfile.FastGFile("C:\\Users\\n8100\\PycharmProjects\\Pneumonia_detection\\myapp\\logsold\\output_graph.pb", 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    _ = tf.import_graph_def(graph_def, name='')


for i in list_p:

    img.append(i)
    labels.append("pneumonia")

for i in list_n:
    img.append(i)
    labels.append("normal")


for i in list_c:
    img.append(i)
    labels.append("covid 19")


for i in img:

    image_data = tf.io.gfile.GFile(i, 'rb').read()

# Loads label file, strips off carriage return

    with tf.Session() as sess:
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        predictions = sess.run(softmax_tensor, \
                               {'DecodeJpeg/contents:0': image_data})
        # Sort to show labels of first prediction in order of confidence
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
        for node_id in top_k:
            human_string = label_lines[node_id]
            score = predictions[0][node_id]
            print('%s (score = %.5f)' % (human_string, score))
            res=human_string
            pred.append(res)
            break


print(pred)
print(labels)

from sklearn.metrics import confusion_matrix

conf_matrix=confusion_matrix(pred,labels)

import  matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(7.5, 7.5))
ax.matshow(conf_matrix, cmap=plt.cm.Blues, alpha=0.3)
for i in range(conf_matrix.shape[0]):
    for j in range(conf_matrix.shape[1]):
        ax.text(x=j, y=i, s=conf_matrix[i, j], va='center', ha='center', size='xx-large')

plt.xlabel('Predictions', fontsize=18)
plt.ylabel('Actuals', fontsize=18)
plt.title('Confusion Matrix', fontsize=18)
plt.show()


from sklearn.metrics import f1_score,precision_score,precision_recall_fscore_support

precision, recall, f1, _ = precision_recall_fscore_support(labels, pred, labels=['pneumonia', 'normal', 'covid 19'])

print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)