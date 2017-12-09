import pandas as pd
from sklearn import metrics
from sklearn.model_selection import train_test_split
import pickle
from xgboost.sklearn import XGBRegressor
from sklearn.preprocessing import StandardScaler
def GDBTTrain(X, y):
    train_x, test_x, train_y, test_y = train_test_split(X, y, test_size=0.5, random_state=0)  ##test_size测试集合所占比例
    test_preds = pd.DataFrame({"label": test_y})
    clf = XGBRegressor(
        learning_rate=0.05,  # 默认0.3
        n_estimators=1200,  # 树的个数
        max_depth=22,
        min_child_weight=1,
        gamma=0.2,
        subsample=0.6,
        colsample_bytree=0.6,
        nthread=4,  # cpu线程数
        scale_pos_weight=1,
        reg_alpha=1e-05,
        reg_lambda=1,
        seed=27
    )
    clf.fit(train_x, train_y)
    test_preds['y_pred'] = clf.predict(test_x)
    stdm = metrics.r2_score(test_preds['label'], test_preds['y_pred'])
    #import matplotlib.pyplot as plt  # 画出预测结果图
    #p = test_preds[['label', 'y_pred']].plot(subplots=True, style=['b-o', 'r-*'])
    #plt.show()
    return stdm, clf


data = pd.read_csv('X_U4.csv')
feature = ['M4_y', 'R4', 'V4_y', 'X4_y', 'TT4', 'AC4', 'E4', 'Z4', 'AA4', 'AI4', 'L4', 'O4']
X = data[feature]
X = X.as_matrix()
y = data['U4']
y = y.as_matrix()
stdm, clf = GDBTTrain(X, y)
print('saving model')
path = './GDmodel/' + 'U4_xgb.pkl'
with open(path, "wb") as f:
    pickle.dump(clf, f)
print(stdm)