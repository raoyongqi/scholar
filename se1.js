const aElements = document.querySelectorAll('#gs_res_ccl_mid a');
const result = [];  // 创建一个空数组，用于存储每个 <a> 元素的信息

aElements.forEach(a => {
    if (a.hasAttribute('id')) {  // 检查是否有 'id' 属性
        const childNodes = [];
        a.childNodes.forEach(child => {
            // 如果是文本节点，直接添加到 childNodes
            if (child.nodeType === Node.TEXT_NODE) {
                childNodes.push(child.nodeValue.trim());  // 获取文本节点的内容
            } 
            // 如果是元素节点，但不是 <b>，则直接添加元素节点的名称
            else if (child.nodeType === Node.ELEMENT_NODE && child.nodeName !== 'B') {
                childNodes.push(child.nodeName);  // 获取元素节点的名称
            } 
            // 如果是 <b> 标签，获取其子节点并添加到 childNodes
            else if (child.nodeName === 'B') {
                child.childNodes.forEach(grandChild => {
                    if (grandChild.nodeType === Node.TEXT_NODE) {
                        childNodes.push(grandChild.nodeValue.trim());  // 获取 <b> 子节点的文本内容
                    } else if (grandChild.nodeType === Node.ELEMENT_NODE) {
                        childNodes.push(grandChild.nodeName);  // 获取 <b> 子节点的元素名称
                    }
                });
            }
        });
        
        
        const aInfo = {
            "href": a.href,  // a元素的文本内容
            "id": a.id,  // a元素的文本内容

            "childNodes": childNodes // a元素的所有子节点
        };

        result.push(aInfo);  // 将每个 aInfo 添加到数组中
    }
});

// 将结果转换为 JSON 格式
const jsonString = JSON.stringify(result, null, 2);  // 格式化输出，使其易于阅读

// 保存到文件（在浏览器中无法直接保存文件，但你可以将其下载为文件）
// 以下是一个用于下载 JSON 的方法
const blob = new Blob([jsonString], { type: 'application/json' });
const link = document.createElement('a');
link.href = URL.createObjectURL(blob);
link.download = 'a_elements.json';
link.click();
